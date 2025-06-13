// There is nothing here actually !!!

// Fetch the languages and store in the global variable
let languages = [];
fetch('/get_languages')
    .then(response => response.json())
    .then(data => {
        languages = data;
        renderLanguageDropdown();
    })
    .catch(error => console.error('Error fetching languages:', error));


// Function to render the dropdown dynamically
function renderLanguageDropdown() {
    // const select = document.createElement('select');
    // select.id = 'languageSelector';
    const select = document.getElementById('language_select');
    select.innerHTML = '';

    // Populate the <select> with options from languages array
    languages.forEach((lang) => {
        const option = document.createElement('option');
        // Set the 'value' = language code, but show the language name
        option.value = lang.code;
        option.textContent = lang.name;
        select.appendChild(option);
    });

    // Set the dropdown to the currently selected language
    setDropdownLanguage();
}


// Function to set the dropdown language based on the query parameter
// This is set up because, after translation, the page is updated, but the dropdown still remains to the default language (English)
function setDropdownLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    const currentLang = urlParams.get('lang') || 'en'; // Default to 'en'
    const select = document.getElementById('language_select');
    select.value = currentLang;
}


// Update the page with change in language:
document.addEventListener('DOMContentLoaded', function () {
    const languageSelect = document.getElementById('language_select');
    // console.log('languageSelect:', languageSelect);

    languageSelect.addEventListener('change', function (e) {
        const selectedLanguage = e.target.value;
        console.log('selectedLanguage:', selectedLanguage);
        const currentPath = window.location.pathname;
        const placeId = currentPath.split('/').pop(); // Gets the ID from URL

        // Only make the fetch call if we're on a place detail page
        if (currentPath.includes('/place/')) {
            const new_url = `/place/${placeId}?lang=${selectedLanguage}`;
            console.log('new_url:', new_url);

            fetch(new_url)
                .then(response => {
                    if (response.ok) {
                        // The server returns rendered template in new language:
                        // Open that in same tab:
                        window.location.href = new_url;
                    }
                })
                .catch(error => console.error('Error:', error));
        }
    });
});


// Responsiveness:
// Add this to your existing script.js
document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger');
    const navRight = document.querySelector('.nav-right');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navRight.classList.toggle('active');
    });
});