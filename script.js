const API = "http://127.0.0.1:5000"

let manaZina = document.querySelector('.manaZina')
let chataZinas = document.querySelector('.chatazinas')



function sutitZinu(){
    console.log("sutitzinu() darbojas")
    // Mainām html lapā vērtību, vizuāli attēlo
    chataZinas.innerHTML += '<br/>' + manaZina.value
    // Veidojam komunikāciju ar python failu
    fetch(API+'/sutit/'+manaZina.value)
}