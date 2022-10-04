const formFields = document.querySelectorAll(".form-input-container");
const baseSideNav = document.querySelector(".base-sidenav");
const container = document.querySelector(".container");
const contentContainer = document.querySelector(".content-container");
const contentFormContainers = document.querySelectorAll(".content-form-container");
const clickCreateFormInputs = document.querySelectorAll(".click-create-form-input");
const formErrors = document.querySelectorAll(".form-errors");
const allErrorList = document.querySelectorAll(".errorlist");
if (formErrors || allErrorList) {
  formErrors.forEach(formError => {
    setTimeout(() => {
      formError.textContent = "";
      formError.classList.add("hide");
    }, 2000);
  });

  allErrorList.forEach(errorList => {
    setTimeout(() => {
      errorList.textContent = "";
      errorList.classList.add("hide");
    }, 2000);
  });
}

if (clickCreateFormInputs) {
  clickCreateFormInputs.forEach(clickCreateFormInput => {
    clickCreateFormInput.addEventListener("click", () => {});
  });
}

if (contentFormContainers) {
  contentFormContainers.forEach(contentFormContainer => {
    contentFormContainer.addEventListener("click", e => {
      contentFormContainer.firstElementChild.classList.add("hide");
      form = contentFormContainer.lastElementChild;
      cancelBtn = contentFormContainer.querySelector("#content-form-cancel-btn");
      form.classList.remove("hide");
      form.style.width = "auto";
      contentFormContainer.style.cursor = "default";

      if (e.target.id == "content-form-cancel-btn") {
        form.classList.add("hide");
        contentFormContainer.firstElementChild.classList.remove("hide");
      }
    });
  });
}

function getContentPageWidth(baseSideNav, container) {
  const containerWidth = container.getBoundingClientRect().width;
  const baseSideNavWidth = baseSideNav.getBoundingClientRect().width;
  remainingWidth = containerWidth - baseSideNavWidth;
  contentContainer.style.width = `${remainingWidth}px`;
}

window.addEventListener("load", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
});

window.addEventListener("resize", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
});

formFields.forEach(formField => {
  formField.addEventListener("keyup", e => {
    const requriedFieldSymbol = formField.querySelector(".form-required-field");
    const formInput = formField.lastElementChild;
    if (requriedFieldSymbol) {
      if (formInput.value) {
        requriedFieldSymbol.classList.add("hide");
      } else {
        requriedFieldSymbol.classList.remove("hide");
      }
    }
  });
});
