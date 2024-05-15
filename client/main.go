package main

import (
	"encoding/json"
	"fmt"
	"github.com/charmbracelet/huh"
	"github.com/charmbracelet/huh/spinner"
	"github.com/charmbracelet/lipgloss"
	"io"
	"net/http"
	"net/url"
	"os"
	"strconv"
	"strings"
)

var (
	userName   string
	crushName  string
	prediction float64
)

type Career int

const (
	Law = iota
	Finance
	Entertainment
	Development
	Enterprise
	Academia
	Policy
	Business
	SocialWork
	Tech
	Healthcare
	Education
	Marketing
	Research
	Other
)

func (c Career) String() string {
	switch c {
	case Law:
		return "Law"
	case Finance:
		return "Finance"
	case Entertainment:
		return "Entertainment"
	case Development:
		return "Development"
	case Enterprise:
		return "Enterprise"
	case Academia:
		return "Academia"
	case Policy:
		return "Policy"
	case Business:
		return "Business"
	case SocialWork:
		return "Social Work"
	case Tech:
		return "Tech"
	case Healthcare:
		return "Healthcare"
	case Education:
		return "Education"
	case Marketing:
		return "Marketing"
	case Research:
		return "Research"
	case Other:
		return "Other"
	default:
		return ""
	}
}

type Data struct {
	gender bool
	age    string
	income string
	career Career
	attr   string // attractiveness
	sinc   string // sincerity
	intel  string // intelligence
	fun    string // fun
	amb    string // ambition
	met    bool
}

type Response struct {
	Prediction float64 `json:"prediction"`
}

func main() {
	var data Data

	// Create a new form
	form := huh.NewForm(
		huh.NewGroup(huh.NewNote().
			Description("Welcome to _MatchMaker_.\n\nThis is a simple application that predicts the compatibility between you and your crush with the power of AI.\n\nPlease answer the following questions to get started.")),
		huh.NewGroup(
			huh.NewInput().
				Value(&userName).
				Title("What is your name?").
				Placeholder("Name"),
			huh.NewInput().
				Value(&crushName).
				Title("What is your crush's name?").
				Placeholder("Name"),
		),
		huh.NewGroup(
			huh.NewConfirm().
				Value(&data.gender).
				Title("Choose your gender").
				Affirmative("Man").
				Negative("Woman"),
			huh.NewInput().
				Value(&data.age).
				Title("How old are you?").
				Placeholder("Age"),
			huh.NewInput().
				Value(&data.income).
				Title("What is your income?").
				Placeholder("Income"),
			huh.NewSelect[Career]().
				Value(&data.career).
				Title("What is your career?").
				Options(
					huh.NewOption("Law", Career(Law)),
					huh.NewOption("Finance", Career(Finance)),
					huh.NewOption("Entertainment", Career(Entertainment)),
					huh.NewOption("Development", Career(Development)),
					huh.NewOption("Enterprise", Career(Enterprise)),
					huh.NewOption("Academia", Career(Academia)),
					huh.NewOption("Policy", Career(Policy)),
					huh.NewOption("Business", Career(Business)),
					huh.NewOption("Social Work", Career(SocialWork)),
					huh.NewOption("Tech", Career(Tech)),
					huh.NewOption("Healthcare", Career(Healthcare)),
					huh.NewOption("Education", Career(Education)),
					huh.NewOption("Marketing", Career(Marketing)),
					huh.NewOption("Research", Career(Research)),
					huh.NewOption("Other", Career(Other)),
				),
		),
		huh.NewGroup(
			huh.NewInput().
				Value(&data.attr).
				Title("How attractive are you?").
				Placeholder("1-10"),
			huh.NewInput().
				Value(&data.sinc).
				Title("How sincere are you?").
				Placeholder("1-10"),
			huh.NewInput().
				Value(&data.intel).
				Title("How intelligent are you?").
				Placeholder("1-10"),
			huh.NewInput().
				Value(&data.fun).
				Title("How fun are you?").
				Placeholder("1-10"),
			huh.NewInput().
				Value(&data.amb).
				Title("How ambitious are you?").
				Placeholder("1-10"),
			huh.NewConfirm().
				Value(&data.met).
				Title("Have you met your crush?").
				Affirmative("Yes").
				Negative("No"),
		),
	).WithTheme(huh.ThemeDracula())

	err := form.Run()

	if err != nil {
		fmt.Println("Uh oh:", err)
		os.Exit(1)
	}

	sendRequest := func() {
		// Send the data to the server
		// gender age income career attr sinc intel fun amb met
		resp, err := http.PostForm("http://localhost:5000/predict",
			url.Values{
				"gender": {strconv.FormatBool(data.gender)},
				"age":    {data.age},
				"income": {data.income},
				"career": {strconv.Itoa(int(data.career))},
				"attr":   {data.attr},
				"sinc":   {data.sinc},
				"intel":  {data.intel},
				"fun":    {data.fun},
				"amb":    {data.amb},
				"met":    {strconv.FormatBool(data.met)}})
		if err != nil {
			fmt.Println("Error:", err)
			os.Exit(1)
		}
		defer func(Body io.ReadCloser) {
			err := Body.Close()
			if err != nil {
				fmt.Println("Error:", err)
				os.Exit(1)
			}
		}(resp.Body)
		body, err := io.ReadAll(resp.Body)
		var result Response
		if err := json.Unmarshal(body, &result); err != nil {
			fmt.Println("Can not unmarshal JSON")
		}
		prediction = result.Prediction
	}

	// Send the data to the server
	_ = spinner.New().Title("Processing...").Action(sendRequest).Run()

	{
		var sb strings.Builder
		keyword := func(s string) string {
			return lipgloss.NewStyle().Foreground(lipgloss.Color("212")).Render(s)
		}
		fmt.Fprintf(&sb,
			"%s\n\n%s and %s are %s compatible.",
			lipgloss.NewStyle().Bold(true).Render(" ♡ PREDICTION ♡"),
			keyword(userName),
			keyword(crushName),
			keyword(strconv.FormatFloat(prediction, 'f', 2, 64)+"%"),
		)

		if prediction > 50 {
			fmt.Fprint(&sb, "\n\nYou have a good chance to be together :>")
		} else {
			fmt.Fprint(&sb, "\n\nYou have a low chance to be together :<")
		}

		fmt.Println(
			lipgloss.NewStyle().
				Width(45).
				BorderStyle(lipgloss.RoundedBorder()).
				Padding(1, 2).
				Render(sb.String()),
		)
	}
}
