const themeSwitcher = document.getElementById('theme-switcher')
const body = document.getElementsByTagName('body')[0]
const card = Array.from(document.getElementsByClassName('card'))

themeSwitcher.checked = true


themeSwitcher.addEventListener('click', () => {
    body.classList.toggle('light')
    card.forEach(item => {
        item.classList.toggle('light')
    })
})