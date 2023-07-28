document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.getElementsByClassName("show-more-button");
  
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener("click", function() {
        var descriptionContainer = this.parentNode.querySelector(".description-container");
        var descriptionTruncated = descriptionContainer.querySelector(".description-truncated");
        var descriptionFull = descriptionContainer.querySelector(".description-full");
  
        if (descriptionContainer.classList.contains("expanded")) {
          descriptionContainer.classList.remove("expanded");
          descriptionTruncated.style.display = "block";
          descriptionFull.style.display = "none";
          this.textContent = "Show more";
        } else {
          descriptionContainer.classList.add("expanded");
          descriptionTruncated.style.display = "none";
          descriptionFull.style.display = "block";
          this.textContent = "Show less";
        }
      });
    }
  });
  