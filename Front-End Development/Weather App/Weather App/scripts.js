document.addEventListener("DOMContentLoaded", function () {
    const apiKey = "9a080c4143d20f0d3cc3fb8d94f8e39c";
    const apiUrl = "https://api.openweathermap.org/data/2.5/weather?";
    let units = "metric";

    const searchBox = document.querySelector(".search input");
    const searchBtn = document.querySelector(".search button");
    const weatherIcon = document.querySelector(".weather-icon");
    const unitToggle = document.querySelector(".unit-toggle");

    async function checkWeather(city) {
        try {
            const response = await axios.get(`${apiUrl}q=${city}&units=${units}&appid=${apiKey}`);
            const data = response.data;

            document.querySelector(".city").innerText = data.name;
            document.querySelector(".temp").innerText = `${Math.round(data.main.temp)}°${units === "metric" ? "C" : "F"}`;
            document.querySelector(".humidity").innerText = `${data.main.humidity}%`;
            document.querySelector(".wind").innerText = `${data.wind.speed} ${units === "metric" ? "km/h" : "mph"}`;

            const weatherMapping = {
                "Clouds": "images/clouds.png",
                "Clear": "images/clear.png",
                "Rain": "images/rain.png",
                "Drizzle": "images/drizzle.png",
                "Mist": "images/mist.png",
                "Snow": "images/snow.png"
            };

            weatherIcon.src = weatherMapping[data.weather[0].main] || "images/default.png";
            document.querySelector(".weather").style.display = "block";
            document.querySelector(".Error").style.display = "none";

        } catch (error) {
            document.querySelector(".Error").style.display = "block";
            document.querySelector(".weather").style.display = "none";
            document.querySelector(".unit-toggle").style.display = "none";
            console.error("Error fetching weather data:", error);
        }
    }

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(async (position) => {
                const { latitude, longitude } = position.coords;
                try {
                    const response = await axios.get(`${apiUrl}lat=${latitude}&lon=${longitude}&units=${units}&appid=${apiKey}`);
                    checkWeather(response.data.name);
                } catch (error) {
                    checkWeather("Lucknow"); 
                }
            }, () => checkWeather("Lucknow"));
        } else {
            checkWeather("Lucknow");
        }
    }

    searchBtn.addEventListener("click", () => checkWeather(searchBox.value));
    
    unitToggle.addEventListener("click", () => {
        units = units === "metric" ? "imperial" : "metric";
        checkWeather(document.querySelector(".city").innerText);
    });

    getLocation();
});
