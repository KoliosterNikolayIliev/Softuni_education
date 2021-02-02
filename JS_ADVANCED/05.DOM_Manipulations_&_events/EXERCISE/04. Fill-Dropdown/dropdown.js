function addItem() {
    let select = document.getElementById('menu')
    let option = document.createElement('option')
    let newText = document.getElementById('newItemText')
    let newValue = document.getElementById('newItemValue')

    option.textContent = newText.value
    option.value = newValue.value
    select.appendChild(option)
    newText.value = ''
    newValue.value = ''
}