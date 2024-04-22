var image1 = document.getElementById("image1");
      if (image1) {
        image1.addEventListener("click", function () {
          var anchor = document.querySelector("[data-scroll-to='heroContainer']");
          if (anchor) {
            anchor.scrollIntoView({ block: "start", behavior: "smooth" });
          }
        });
}

document.querySelector('.menu').addEventListener('click', function() {
  var navLinks = document.querySelector('.nav-links');
  if (navLinks.style.display === "none") {
    navLinks.style.display = "flex";
  } else {
    navLinks.style.display = "none";
  }
});
      
var about = document.getElementById("about");
      if (about) {
        about.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
}
      
var navAbout = document.getElementById("navAbout");
      if (navAbout) {
        navAbout.addEventListener("click", function (e) {
          window.location.href = "./about.html";
        });
}
      
var ourServices = document.getElementById("ourServices");
      if (ourServices) {
        ourServices.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
}
      
var navServices = document.getElementById("navServices");
      if (navServices) {
        navServices.addEventListener("click", function (e) {
          window.location.href = "./services.html";
        });
}
      
var blog = document.getElementById("blog");
      if (blog) {
        blog.addEventListener("click", function (e) {
          window.location.href = "./blog.html";
        });
}
      
var navBlog = document.getElementById("navBlog");
      if (navBlog) {
        navBlog.addEventListener("click", function (e) {
          window.location.href = "./blog.html";
        });
}
      
var contact = document.getElementById("contact");
      if (contact) {
        contact.addEventListener("click", function (e) {
          window.location.href = "./contact.html";
        });
}
      
var navContact = document.getElementById("navContact");
      if (navContact) {
        navContact.addEventListener("click", function (e) {
          window.location.href = "./contact.html";
        });
}
      
var navButton = document.getElementById("navButton");
      if (navButton) {
        navButton.addEventListener("click", function (e) {
          window.location.href = "./project.html"
      });
}
      
var getStartedButton = document.getElementById("getStartedButton");
      if (getStartedButton) {
        getStartedButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
      });
}
      
var learnMoreButton = document.getElementById("learnMoreButton");
      if (learnMoreButton) {
        learnMoreButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
      });
}
      
var aboutButton = document.getElementById("aboutButton");
      if (aboutButton) {
        aboutButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
}
      
var quoteButton = document.getElementById("quoteButton");
      if (quoteButton) {
        quoteButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
}
      
var servicesButton = document.getElementById("servicesButton");
      if (servicesButton) {
        servicesButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
}
      
      var contactButton = document.getElementById("contactButton");
      if (contactButton) {
        contactButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
      }
      
      var frame11 = document.getElementById("frame11");
      if (frame11) {
        frame11.addEventListener("click", function (e) {
          window.location.href = "./blog-post2.html";
        });
      }
      
      var frame3 = document.getElementById("frame3");
      if (frame3) {
        frame3.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
      }
      
      var frame21 = document.getElementById("frame21");
      if (frame21) {
        frame21.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
      }
      
      var jakLogoContainer = document.getElementById("jakLogoContainer");
      if (jakLogoContainer) {
        jakLogoContainer.addEventListener("click", function () {
          var anchor = document.querySelector("[data-scroll-to='heroContainer']");
          if (anchor) {
            anchor.scrollIntoView({ block: "start", behavior: "smooth" });
          }
        });
      }
      
      var linkHome = document.getElementById("linkHome");
      if (linkHome) {
        linkHome.addEventListener("click", function () {
          var anchor = document.querySelector("[data-scroll-to='heroContainer']");
          if (anchor) {
            anchor.scrollIntoView({ block: "start", behavior: "smooth" });
          }
        });
      }
      
      var linkAbout = document.getElementById("linkAbout");
      if (linkAbout) {
        linkAbout.addEventListener("click", function (e) {
          window.location.href = "./about.html";
        });
      }
      
      var linkContact = document.getElementById("linkContact");
      if (linkContact) {
        linkContact.addEventListener("click", function (e) {
          window.location.href = "./contact.html";
        });
      }
      
      var linkBlog = document.getElementById("linkBlog");
      if (linkBlog) {
        linkBlog.addEventListener("click", function (e) {
          window.location.href = "./blog.html";
        });
      }
      
      var linkBlog = document.getElementById("linkBlog");
      if (linkBlog) {
        linkBlog.addEventListener("click", function (e) {
          window.location.href = "./services.html";
        });
      }
      
      var linkFAQs = document.getElementById("linkFAQs");
      if (linkFAQs) {
        linkFAQs.addEventListener("click", function (e) {
          window.location.href = "./jak-faqs.html";
        });
      }
      
      var footerButton = document.getElementById("footerButton");
      if (footerButton) {
        footerButton.addEventListener("click", function (e) {
          window.location.href = "./component.html";
        });
      }

      

      let currentSlide = 0;
const testimonials = document.querySelectorAll('.testimonial-item');
const testimonialItems = document.querySelector('.testimonial-items');

function showSlide(index) {
    const slideWidth = testimonials[0].offsetWidth;
    testimonialItems.style.transform = `translateX(-${index * slideWidth}px)`;
}

function changeTestimonial(n) {
    currentSlide += n;
    if (currentSlide < 0) {
        currentSlide = testimonials.length - 1;
    } else if (currentSlide >= testimonials.length) {
        currentSlide = 0;
    }
    showSlide(currentSlide);
}

// Show the initial slide
showSlide(currentSlide);

document.addEventListener("DOMContentLoaded", function() {
    const newsletterForm = document.getElementById('newsletterForm');

    newsletterForm.addEventListener("submit", event => {
        event.preventDefault();

        const emailInput = newsletterForm.querySelector('input[type="email"]');
        const email = emailInput.value;

        if (!email) {
            alert("Please enter your email address.");
            return;
        }

        const data = {
            email: email
        };

        fetch('http://localhost:8000/subscriber/create/', {
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: "POST",
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert("Subscription successful!"); // You can customize this message
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred. Please try again later."); // You can customize this message
        });
    });
});
