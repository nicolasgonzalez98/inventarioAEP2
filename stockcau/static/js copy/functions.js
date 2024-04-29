
let button = document.getElementById('tocar')
let formulario = document.getElementById('filterHardware')

button.addEventListener('click', () => {
    const params = {
        headers : {
            "content-type":'aplication/json; charset=UTF-8'
        }
    }

    fetch('/get-info', params)
    .then(data => data.json())
    .then(res => console.log(res))
    .catch(res => console.log('Hubo un error'))
});

formulario.onchange(() => {
    console.log('gggg')
})