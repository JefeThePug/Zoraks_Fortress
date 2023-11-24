document.addEventListener('DOMContentLoaded', function() {
    const formElement = document.querySelector('.input');
    
    formElement.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        const storyElement = document.querySelector('.story');
        const inputBar = formElement.querySelector('#cmd');
        const innerHTML = storyElement ? storyElement.innerHTML : '';

        if (innerHTML) {
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'command': inputBar.value,
                    'inner_html': innerHTML,
                }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.text();
            })
            .then(html => {
                storyElement.innerHTML = html;
                storyElement.scrollTop = storyElement.scrollHeight;
                inputBar.value = "";
                inputBar.focus();
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } else {
            console.error('Unable to find element with class "story" or inner HTML is empty.');
        }
    });
});
