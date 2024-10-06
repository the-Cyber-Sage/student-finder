import streamlit as st
import requests
import pandas as pd

# Function to fetch data using POST request
def fetch_teacher_data(url, payload):
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON content
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []

# Function to fetch HTML for student data
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text  # Return the HTML content as text
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return ""

# Function to parse HTML and extract student data
def parse_html(html_content):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')

    roll_numbers = []
    names = []
    student_phones = []
    parent_phones = []
    images = []

    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 5:  # Ensure there are enough columns
            roll_numbers.append(columns[1].text.strip())
            names.append(columns[2].text.strip())
            student_phones.append(columns[3].text.strip())
            parent_phones.append(columns[4].text.strip())
            img_tag = columns[0].find('img')
            images.append(img_tag['src'].strip() if img_tag and 'src' in img_tag.attrs else "")

    return roll_numbers, names, student_phones, parent_phones, images

st.title("Student Finder")

clg = st.sidebar.selectbox('Select College', ('NGIT', 'KMEC'))
year = st.sidebar.selectbox('Select Year', ('select', '1', '2', '3', '4'))
branch = st.sidebar.selectbox('Select Branch', ('select', 'CSE', 'CSM', 'CS (only for 2023-2024 batch)'))

if year == 'select':
    st.write("Select YEAR")
if branch == 'select':
    st.write("Select BRANCH")

if clg == 'NGIT' and year != 'select' and branch != 'select':
    url = None

    if year == '1' and branch == 'CSE':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=1&branch=CSE&section=all"
    elif year == '1' and branch == 'CSM':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=1&branch=CSM&section=all"
    elif year == '2' and branch == 'CS (only for 2023-2024 batch)':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=2&branch=CS&section=all"
    if year == '2' and branch == 'CSE':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=2&branch=CSE&section=all"
    elif year == '2' and branch == 'CSM':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=2&branch=CSM&section=all"
    if year == '3' and branch == 'CSE':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=3&branch=CSE&section=all"
    elif year == '3' and branch == 'CSM':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=3&branch=CSM&section=all"
    if year == '4' and branch == 'CSE':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=4&branch=CSE&section=all"
    elif year == '4' and branch == 'CSM':
        url = "https://teleuniv.net.in/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=4&branch=CSM&section=all"

    if url:
        html_content = fetch_html(url)
        roll_numbers, names, student_phones, parent_phones, images = parse_html(html_content)

        data = {
            "Roll No": roll_numbers,
            "Student Name": names,
            "Student Phone": student_phones,
            "Parent Phone": parent_phones,
            "Image": images
        }
        df = pd.DataFrame(data)

        st.dataframe(df)

if clg == 'KMEC' and year != 'select' and branch != 'select':
    url = None

    if year == '1' and branch == 'CSE': 
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=1&branch=CSE&section=all"
    elif year == '1' and branch == 'CSM':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=1&branch=CSM&section=all"
    elif year == '2' and branch == 'CS (only for 2023-2024 batch)':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=2&branch=CS&section=all"
    if year == '2' and branch == 'CSE':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=2&branch=CSE&section=all"
    elif year == '2' and branch == 'CSM':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=2&branch=CSM&section=all"
    if year == '3' and branch == 'CSE':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=3&branch=CSE&section=all"
    elif year == '3' and branch == 'CSM':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=3&branch=CSM&section=all"
    if year == '4' and branch == 'CSE':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=4&branch=CSE&section=all"
    elif year == '4' and branch == 'CSM':
        url = "http://teleuniv.net.in:81/trinetra/pages/lib//student_ajaxfile.php?mid=8&year=4&branch=CSM&section=all"

    if url:
        html_content = fetch_html(url)
        roll_numbers, names, student_phones, parent_phones, images = parse_html(html_content)

        data = {
            "Roll No": roll_numbers,
            "Student Name": names,
            "Student Phone": student_phones,
            "Parent Phone": parent_phones,
            "Image": images
        }
        df = pd.DataFrame(data)

        st.dataframe(df)

# Toggle to View Teacher Information
view_teachers = st.sidebar.checkbox("View Teacher Information")

if view_teachers:
    st.header("Teacher Information")

    # Define the teacher API URL and payload
    teacher_url = "https://teleuniv.net.in/netra/sendsmslib.php"  # Replace with your actual teacher API URL
    payload = {
        "mid": 23
    }

    # Fetch teacher data using POST request
    teachers_data = fetch_teacher_data(teacher_url, payload)

    if teachers_data:
        # Extract relevant fields
        teacher_names = [teacher["teachername"] for teacher in teachers_data]
        usernames = [teacher["username"] for teacher in teachers_data]
        passwords = [teacher["password"] for teacher in teachers_data]

        # Create DataFrame
        teacher_data = {
            "Teacher Name": teacher_names,
            "Username": usernames,
            "Password": passwords
        }
        teacher_df = pd.DataFrame(teacher_data)

        # Display teacher information
        st.dataframe(teacher_df)
    else:
        st.write("No teacher data found.")
