// Global variables
let S3_BASE_URL;
let countries = [];
let places = [];
let currentCountryCode = "IN"; // Default to India (used for initial load)

document.addEventListener('DOMContentLoaded', () => {
    initializeS3BaseUrl();
    initializeLanguages();
    initializeCountries();
    initializePlaces(currentCountryCode);

    setupEventListeners();
});

// ----------------------------------------------------------------------------------
// Initialize S3 Base URL
// ----------------------------------------------------------------------------------
function initializeS3BaseUrl() {
    fetch('/get_s3_base_url')
        .then(response => response.json())
        .then(data => {
            S3_BASE_URL = data;
        })
        .catch(error => console.error('Error fetching S3 base URL:', error));
}

// ----------------------------------------------------------------------------------
// Initialize Languages
// ----------------------------------------------------------------------------------
function initializeLanguages() {
    fetch('/get_languages')
        .then(response => response.json())
        .then(data => {
            renderLanguageDropdown(data);
        })
        .catch(error => console.error('Error fetching languages:', error));
}

// Render language dropdown
function renderLanguageDropdown(languages) {
    const select = document.getElementById('language_select');
    select.innerHTML = '';

    languages.forEach(lang => {
        const option = document.createElement('option');
        option.value = lang.code;
        option.textContent = lang.name;
        select.appendChild(option);
    });
}

// ----------------------------------------------------------------------------------
// Change country name in the header:
// ----------------------------------------------------------------------------------
function updateCountryName(countryCode, countryName) {
    const countryNameHeader = document.getElementById('title_main');

    // iterate over countries to get flag:
    let flag;
    countries.forEach(country => {
        if (country.code === countryCode) {
            flag = country.flag;
        }
    });


    if (countryCode.toLowerCase() === 'all') {
        countryNameHeader.textContent = `Discover Most Beautiful Places of World ${flag}`;
    }
    else {
        countryNameHeader.textContent = `Discover Most Beautiful Places of ${countryName} ${flag}`;
    }
}


// ----------------------------------------------------------------------------------
// Initialize Countries
// ----------------------------------------------------------------------------------
function initializeCountries() {
    fetch('/get_countries')
        .then(response => response.json())
        .then(data => {
            countries = data;
            console.log(countries);
            renderCountryDropdown();
        })
        .catch(error => console.error('Error fetching countries:', error));
}

// Render country dropdown
function renderCountryDropdown() {
    const dropdown = document.getElementById('country_dropdown');
    dropdown.innerHTML = '';

    countries.forEach(country => {
        const div = document.createElement('div');
        div.className = 'country-option';
        div.textContent = country.name;
        div.addEventListener('click', () => {
            selectCountry(country.code, country.name);
        });
        dropdown.appendChild(div);
    });
}

// Handle country selection
function selectCountry(code, name) {
    currentCountryCode = code;

    const searchInput = document.getElementById('country_search');
    searchInput.value = name;
    document.getElementById('country_dropdown').style.display = 'none';

    // Re-fetch locations for the selected country
    initializePlaces(code);

    // Update country name in the header:
    updateCountryName(code, name);
}

// Filter countries by search input
function filterCountries(searchText) {
    const dropdown = document.getElementById('country_dropdown');
    dropdown.style.display = 'block';

    const filteredCountries = countries.filter(country =>
        country.name.toLowerCase().includes(searchText.toLowerCase())
    );

    dropdown.innerHTML = '';
    filteredCountries.forEach(country => {
        const div = document.createElement('div');
        div.className = 'country-option';
        // div.textContent = `${country.name} (${country.code})`;
        div.textContent = `${country.name}`;
        div.addEventListener('click', () => selectCountry(country.code, country.name));
        dropdown.appendChild(div);
    });
}

// ----------------------------------------------------------------------------------
// Initialize Places
// ----------------------------------------------------------------------------------
function initializePlaces(countryCode) {
    const placesContainer = document.getElementById('placesContainer');
    placesContainer.innerHTML = '<div class="loading">Loading places...</div>';

    fetch(`/get_all_locations?country=${countryCode}`)
        .then(response => response.json())
        .then(data => {
            places = data;

            // Render places
            placesContainer.innerHTML = '';
            places.forEach(place => {
                placesContainer.appendChild(createPlaceCard(place));
            });
        })
        .catch(error => console.error('Error fetching places:', error));
}

// Create a place card
function createPlaceCard(loc) {
    const card = document.createElement('div');
    card.className = 'place-card';
    card.innerHTML = `
        <!-- Using Flask 
        -->
        <img src="/get_img/${loc.image}" alt="${loc.name}" class="place-image">
        <img src="/get_img/${loc.image}" alt="${loc.name}" class="place-bg-image">

        <!-- Using S3 
        <img src="${S3_BASE_URL}/${loc.image}" alt="${loc.name}" class="place-image">
        <img src="${S3_BASE_URL}/${loc.image}" alt="${loc.name}" class="place-bg-image">
        -->

        <div class="place-info">
            <h2>${loc.name}</h2>
            <p>${loc.location}</p>
        </div>
    `;

    // Add click event for place details
    card.addEventListener('click', () => {
        window.location.href = `/place/${loc.id}`;
    });

    return card;
}

// ----------------------------------------------------------------------------------
// Event Listeners
// ----------------------------------------------------------------------------------
function setupEventListeners() {
    const searchInput = document.getElementById('country_search');

    // Filter countries as the user types
    searchInput.addEventListener('input', (e) => {
        filterCountries(e.target.value);
    });

    // Show dropdown on focus
    searchInput.addEventListener('focus', () => {
        document.getElementById('country_dropdown').style.display = 'block';
    });

    // Close dropdown on outside click
    document.addEventListener('click', (e) => {
        if (!e.target.closest('#country_search') && !e.target.closest('#country_dropdown')) {
            document.getElementById('country_dropdown').style.display = 'none';
        }
    });

    // Hamburger menu for responsiveness
    const hamburger = document.querySelector('.hamburger');
    const navRight = document.querySelector('.nav-right');
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navRight.classList.toggle('active');
    });
}
