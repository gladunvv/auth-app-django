const themeSwitcher = document.getElementById("theme-switcher");
const body = document.getElementsByTagName("body")[0];
const card = Array.from(document.getElementsByClassName("card"));

try {
  const isLightTheme = window.localStorage.getItem("light");

  if (isLightTheme) {
    themeSwitcher.checked = true;
  } else {
    themeSwitcher.checked = false;
  }
} catch (error) {
  console.log(error);
}

const switchTheme = () => {
  body.classList.toggle("light");
  card.forEach(item => {
    item.classList.toggle("light");
  });
};

window.addEventListener("DOMContentLoaded", () => {
  try {
    const isLightTheme = window.localStorage.getItem("light");
    if (isLightTheme) switchTheme();
  } catch (error) {
    console.log(error);
  }
  
  themeSwitcher.addEventListener("click", () => {
    try {
      const isLightThemeSeted = window.localStorage.getItem("light");
      if (isLightThemeSeted) {
        window.localStorage.removeItem("light");
      } else {
        window.localStorage.setItem("light", "true");
      }
    } catch (error) {
      console.log(error);
    }
    switchTheme();
  });
});

