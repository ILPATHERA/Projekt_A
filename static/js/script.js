        // Submit form data using AJAX
        document.getElementById("form").addEventListener('submit', function(event){
            event.preventDefault();
            var form_data = new FormData(document.getElementById("form"));
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/predict', true);
            xhr.onload = function () {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    document.getElementById("predicted_class").innerHTML = response['prediction'];
                }
            };
            xhr.send(form_data);
        });
        
        // Show uploaded image
        const imageInput = document.getElementById("image");
        const uploadedImage = document.getElementById("uploaded-image");
        const imageContainer = document.getElementById("image-container");
        
        imageInput.addEventListener("change", (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    uploadedImage.src = e.target.result;
                    uploadedImage.style.display = "block";
                    imageContainer.style.display = "flex";
                };
                reader.readAsDataURL(file);
            }
            else {
                uploadedImage.style.display = "none";
                imageContainer.style.display = "none";
            }
        });

    function showAnswer() {
      document.getElementById("predicted_class").style.display = "block";
      document.getElementsByTagName("h3")[0].style.display = "block";
    }