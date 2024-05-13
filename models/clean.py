import pandas as pd


def categorize_career(item):
    if item in law:
        return 0
    if item in finance:
        return 1
    if item in entertainment:
        return 2
    if item in development:
        return 3
    if item in enterprise:
        return 4
    if item in academia:
        return 5
    if item in policy:
        return 6
    if item in business:
        return 7
    if item in social_work:
        return 8
    if item in tech:
        return 9
    if item in healthcare:
        return 10
    if item in education:
        return 11
    if item in marketing:
        return 12
    if item in research:
        return 13
    return 14


law = ['lawyer', 'law', 'Corporate Lawyer', 'Lawyer', 'Corporate attorney', 'LAWYER', 'attorney',
       'Lawyer or professional surfer', 'Law or finance', 'lawyer/gov.position', 'IP Law', 'Law', 'lawyer/policy work',
       'Intellectual Property Attorney', 'attorney?', 'Corporate law', 'tax lawyer', 'Assistant District Attorney']

finance = ['Economist', 'research/financial industry', 'Financial Services', 'Banking', 'Capital Markets',
           'banker / academia', 'banker', 'Private Equity Investing', 'Investment Banking', 'Trading', 'Finance',
           'Asset Management', 'investment banking', 'finance', 'Real Estate/ Private Equity', 'Real Estate',
           'financial service or fashion', 'Private Equity', 'Investment Management', 'corporate finance', 'banking',
           'Trader', 'Wall Street Economist', 'Venture Capital/Consulting/Government', 'Investment banking',
           'International Development banker', 'Corporate Finance, Asset Management/ Hedge Funds',
           'Real Estate Consulting', 'investment management', 'Finance Related',
           'Financial Mathematics-Investment Bank or Hedge Fund-Derivatives Quant Analyst',
           'Work in an investment bank',
           'Money Management', 'Public Finance', 'private equity', 'Health care finance',
           'Fixed Income Sales & Trading',
           'Finance/Economics'  'Trade Specialist', 'finance or engineering', 'Investment Banker',
           'Private Equity - Leveraged Buy-Outs', 'To go into Finance']

entertainment = ['Journalist', "Clidren's TV", 'Music production', 'comedienne', 'novelist', 'Journalism',
                 'film', 'Writer'  'Porn Star', 'Paper Back Writer',
                 'Poet, Writer, Singer, Policy Maker with the UN and/or Indian Govt.', 'WRITING',
                 'manage a museum or art gallery', 'Entertainment/Sports', 'Entertainment/Media',
                 'Art educator and Artist', 'Film/Television', 'Writing', 'Museum Work (Curation?)',
                 'Music Industry', 'music educator, performer', 'Artist'  'Art Management', 'writer',
                 'playing music', 'writer/teacher', 'Writer/journalist', 'Acting', 'Writer/Editor',
                 'journalism', 'Actress', 'film and radio', 'Film', 'film directing', 'Screenwriter',
                 'Filmmaker', 'Writer/teacher', 'Writing or Editorial', 'writer/editor', 'boxing champ',
                 'producer at a non-profit regional theatre', 'writer/producer', 'Pro Beach Volleyball']

development = ['Architecture and design', 'international development work', 'Urban Planner', 'Civil Engineer',
               'Development work on field in the middle of nowhere', 'Development work', 'International Development',
               'Intl Development']

enterprise = ['Organizational Change Consultant', 'consulting', 'Management Consulting' 'management consulting',
              'Consulting', 'consultant', 'Consulting, later Arts or Non-Profit', 'Consultin \\ Management',
              'Business Consulting', 'CONSULTING', 'Management Consultant']

academia = ['Academia, Research, Banking, Life', 'academics or journalism', 'Professor', 'Academic', 'academia',
            'Professor of Media Studies', 'Academic or Research staff', 'University Professor',
            'no idea, maybe a professor', 'professor', 'Professor and Government Official',
            'physicist, probably academia', 'academics', 'academic research', 'college art teacher', 'academic',
            'academician', 'Historian', 'college professor', 'Professor or Consultant', 'History Professor',
            'Academic (Law)',
            'Academia', 'professor, poet/critic', 'College Professor', 'professor of education',
            'academic or consulting',
            'Academia or UN'  'professor in college', 'Academia; Research; Teaching', 'Professor or journalist',
            'to get Ph.D and be a professor', 'Early Childhood Ed. - College/univ. faculity', 'University President',
            'Academic Work, Consultant', 'Academic/ Finance', 'Professor...?', 'acadeic', 'Professor, or Engineer',
            'Professor; Human Rights Director', 'Director of Admissions']

policy = ['Congresswoman, and comedian', 'To create early childhood intervention programs', 'Nonprofit',
          'health policy',
          'Child Rights', 'UN Civil Servant', 'Humanitarian Affairs/Human Rights',
          'International affairs related career',
          'public service', 'Educational Policy', 'president', 'Education Policy Analyst', 'Diplomat',
          'Literacy Organization head/ Director of Development for non-profit', 'curriculum developer',
          'Program development / policy work', 'Security Policy - Homeland Defense', 'GOVERNOR',
          'Social Services/ Policy',
          'Political Development in Africa', 'Social Work Policy', 'Fundraising for Non-Profits', 'politics',
          'Economic Policy Advisor on Latin America', 'Work at the UN', 'Foreign Service',
          'Exec. Director of social service non-profit',
          'reorganizing society. no, I am not being flip.' "Diplomat / Int'l civil servant", 'Diplomat/Business']

business = ['ceo', 'CEO', 'Entrepreneur', 'Microfinancing Program Manager', 'Business - Investment Management',
            'business',
            'Director of Training and Development', 'CEO in For Profit Biomedical Organization', 'enterpreneur',
            'Industry CTO/CEO',
            "Int'l Business", 'General Management', 'Media Management', 'Energy Management', 'Business Management',
            'Business/Law',
            'Entrepreneurship', 'Management', 'General management/consulting',
            'Business Management and Information Technology',
            'entrepeneur', 'Business', 'International Business', 'M&A Advisory', 'MBA']

social_work = ['health/nutrition oriented social worker', 'Social Worker', 'Social work with children',
               'Social Work Administration', 'social worker' 'Social Worker.... Clinician', 'Clinical Social Worker',
               'Social work', 'Social Work']

tech = ['Informatics', 'tech professional' 'Engineer', 'Engineer or iBanker or consultant', 'Engineering',
        'Ph.D. Electrical Engineering', 'industrial scientist', 'Mechanical Engineering', 'Biotech/business',
        'Energy', 'ASIC Engineer', 'software engr, network engr', 'Science', 'biology industry',
        'engineering professional']

healthcare = ['psychologist', 'Speech Language Pathologist', 'Medicine', 'pharmaceuticals', 'Cardiologist',
              'Pediatrics',
              'medicine', 'Neuroscientist/Professor', 'pharmaceuticals and biotechnology', 'Physician Scientist',
              'Epidemiologist',
              'Psychologist', 'Academic Physician', 'nutrition and dental', 'Physician', 'dietician',
              'doctor and entrepreneur',
              'Pharmaceuticals/Consulting', 'speech pathologist', 'Speech Pathologist',
              'clinical psychologist, researcher, professor',
              'school psychologist', 'School Psychologist', 'medical examiner or researcher', 'Healthcare',
              'Nutritionist', 'epidemiologist',
              'Private practice Dietician', 'Clinical Psychology', 'Clinical Psychologist', 'physician, informaticist',
              'physician', 'Clinic Trial', 'Doctor', 'physician/healthcare', 'Sex Therapist', 'Medical Sciences']

education = ['teacher', 'Counseling Adolescents', 'teaching and then...', 'Education Administration',
             'Teacher/Professor',
             'teaching', 'Education', 'education', 'elementary school teacher', 'Conservation training and education',
             'Teacher',
             'Secondary Education Teacher', 'High School Social Studies Teacher', 'English Teacher', 'Educator',
             'teaching/education', 'I am a teacher.', 'EDUCATION ADMINISTRATION', 'Elementary Education Teaching',
             'School Counseling', 'Elementary school teacher', 'Public School Principal',
             'Bilingual Elementary School Teacher',
             'teacher and performer', 'School Leadership/Politics', 'TEACHING', 'English teacher']

marketing = ['Marketing', 'Marketing, Advertising', 'Marketing and Media', 'Brand Management',
             'marketing / brand management',
             'Marketing or Strategy and Business Development', 'Media Marketing/Entrepreneurship']

research = ['Operations Research', 'Biostatistics', 'Economic research', 'Research Scientist',
            'research in industry or academia', 'a research position', 'research', 'Research scientist, professor',
            'Country Analysis/Research/Credit Analysis', 'scientific research', 'Researcher', 'Research/Teaching',
            'researcher in sociology', 'scientist', 'Naturalist', 'researcher/academia', 'Scientist',
            'Scientist/educator', 'scientific research for now but who knows',
            'research position in pharmaceutical industry', 'research/academia', 'research - teaching', 'Research',
            'researcher', 'Research Engineer']


def get_data():
    # Reading the data
    missing_values = ("n/a", "na", "--", '-')
    df = pd.read_csv("../data.csv", na_values=missing_values)

    # Dropping 'goal' and 'like' column
    df = df.drop('goal', axis=1)
    df = df.drop('like', axis=1)
    df = df.drop('shar', axis=1)
    df = df.drop('prob', axis=1)

    # Categorizing career
    df["career"] = df["career"].apply(categorize_career)

    # Filling missing values
    df["age"] = df["age"].fillna(df["age"].median())
    df["income"] = df["income"].fillna(df["income"].median())
    df["attr"] = df["attr"].fillna(df["attr"].median())
    df["intel"] = df["intel"].fillna(df["intel"].median())
    df["sinc"] = df["sinc"].fillna(df["sinc"].median())
    df["fun"] = df["fun"].fillna(df["fun"].median())
    df["amb"] = df["amb"].fillna(df["amb"].median())
    # df["shar"] = df["shar"].fillna(df["shar"].median())
    # df["prob"] = df["prob"].fillna(df["prob"].median())
    df["met"] = df["met"].fillna(df["met"].median())

    # Normalizing the data
    df["met"] = df["met"].apply(lambda x: 1 if x > 5 else 0)

    return df
