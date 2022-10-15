// A função deve receber um objeto com as propriedades a seguir, e suas 
// devidas restrições:

// STRING name - Deve ter pelo menos 3 letras, e no máximo 10
// STRING title - É opcional, mas quando passada deve ter exatamente 2 
// letras
// INTEGER age - Deve ser um número inteiro entre 18 e 60 (ambos os valores 
// inclusos)

// Caso todos os campos estejam corretos, a função deve retornar uma string 
// vazia
//  *
// A função deve retornar uma string com as mensagens de erros, caso existam.
// Mensagens de erro:
// name inexistente: "name is required"
// name com tamanho fora do determinado: "name need to be in range"
// title inexistente: "title length need to be 2 or undefined"
// age inexistente: "age is required"
// age fora da faixa determinada: "age need to be in range"

function isUserValid(user) { 
    const {name = '', title='', age=0} = user 
   
    if(!name) return `name is required` 
    if(name.length > 10 || name.length < 3) return 'name need to be in range' 
    if(!([0,2].includes(title.length))) return 'title length need to be 2 or undefined or a empty string' 
    if(!age) return `age is required` 
    if(age < 18 || age > 60) return 'age need to be in range' 
    return '' 
  }