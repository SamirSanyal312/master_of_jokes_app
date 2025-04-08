# Master of Jokes

Master of Jokes is a Flask-based web application that lets users share, view, and rate jokes in a unique exchange system inspired by the concept:

> _"Have a penny, leave a penny. Need a penny, take a penny."_

Users earn joke credits by contributing jokes and spend them to view jokes submitted by others.

## 🚀 Features

- 🔐 **User Authentication**
- 📝 **Leave a Joke**
- 📚 **My Jokes**
- 😂 **Take a Joke**
- ⭐ **Rate Jokes**

## 🧪 How to Run (Dev Mode)

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database and run the app:

   ```bash
   flask --app app init-db
   flask --app app run --debug
   ```

   Visit `http://127.0.0.1:5500` in your browser.

## 🐳 Deploy with Docker

1. Clone the repository:

   ```bash
   git clone https://github.iu.edu/SE-Team-6/master-of-jokes.git
   cd master-of-jokes
   ```

2. Build the Docker image:

   ```bash
   docker build -t master-of-jokes .
   ```

3. Run the container:

   ```bash
   docker run -P master-of-jokes
   ```

   Access the app at: `http://127.0.0.1:5500`
