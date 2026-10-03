const form = document.getElementById("urlForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const url = document.getElementById("urlInput").value;

    result.innerHTML = "Creating short URL...";

    try {
        const response = await fetch("/shorten", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

        if (response.ok) {
            result.innerHTML = `
                <p><strong>Short URL:</strong></p>
                <a href="${data.short_url}" target="_blank">
                    ${data.short_url}
                </a>
            `;
        } else {
            result.innerHTML = `
                <p class="error">${data.error}</p>
            `;
        }

    } catch (error) {
        result.innerHTML = `
            <p class="error">Something went wrong. Please try again.</p>
        `;
    }
});