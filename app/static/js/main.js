document.addEventListener("DOMContentLoaded", function () {
    // Get all script links
    const scriptLinks = document.querySelectorAll(".script-link");
  
    // Add click event listener to each script link
    scriptLinks.forEach((link) => {
      link.addEventListener("click", function (event) {
        event.preventDefault();
        runPythonScript(link.dataset.script);
      });
    });
  });
  
  // Function to run a Python script and display the output in the console
  function runPythonScript(scriptName) {
    // Replace this with the actual API call to run the Python script
    fetch(`/run-script/${scriptName}`)
      .then((response) => response.text())
      .then((output) => {
        // Display the output in the console
        const consoleElement = document.querySelector(".console");
        consoleElement.textContent = output;
      })
      .catch((error) => {
        console.error("Error running Python script:", error);
      });
  }
  