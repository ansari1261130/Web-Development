**Overview**
This Weather App allows users to fetch real-time weather data for a specified location. It supports geolocation-based weather fetching and includes a unit toggle between Celsius and Fahrenheit.

**Features**
🌦 Fetch real-time weather data using an API.
📍 Geolocation support to get the user's current weather.
🔄 Unit toggle between Celsius and Fahrenheit.
📱 Responsive UI design.
⚠️ Error handling for API failures and incorrect inputs.

**Usage**
Enter a city name in the search bar and press enter.
Click on the unit toggle button to switch between Celsius and Fahrenheit.
If prompted, allow location access to fetch weather data based on your current location.

**Approach and Challenges**

Approach
Used HTML, CSS, and JavaScript for the front-end.
Integrated a weather API to fetch real-time weather data.
Implemented geolocation to detect the user's current location.
Designed a responsive UI using CSS flexbox and media queries.
Added error handling for invalid city names, API failures, and geolocation permission denials.

Challenges and Solutions
Challenge: Handling API errors when the city name is incorrect or the request fails.
Solution: Implemented try-catch blocks and displayed user-friendly error messages.
Challenge: Dealing with geolocation permission denial.
Solution: Displayed a fallback message allowing users to enter a city manually.
Challenge: Ensuring responsive design across different devices.
Solution: Used media queries and flexible CSS layouts.

**Technologies Used**
HTML, CSS, JavaScript for front-end development.
Fetch API to retrieve weather data.
Geolocation API for location-based weather fetching.
