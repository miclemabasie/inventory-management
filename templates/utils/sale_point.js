console.log('We are in with JavaScript')
form = document.getElementById('add-sale')

const product = document.getElementById('id_product')
const quantity = document.getElementById('id_quantity')
const price = document.getElementById('id_price')
const created = document.getElementById('id_date')
const url = '/sales/sales-point/'
const sBtn = document.getElementById('set-sale-btn')
let salesTable = document.getElementById('sale-point-table')


const calCulatePrice = (quantity, unitPrice) => {
  let totalPrice = quantity * unitPrice
  return totalPrice
}

const calculateIndex = (table) => {
  var tabIndex =  salesTable.rows.length
  return tabIndex
}

{/* Create delete button */}


const updateTabeleRow = (resData, table) => {
  salesTable.innerHTML += `<tr>
  <th scope="row">${calculateIndex(table)}</th>
  <td>${resData.product}</td>
  <td>${resData.quantity}</td>
  <td>${resData.price}</td>
  <td>${calCulatePrice(resData.quantity, resData.price)}</td>
  <td class="position_id">${resData.position_id}</td>
  <td><button class="btn btn-danger btn-sm delete">X</button></td>
</tr>`
} 

if (e.target.classList.contains('delete')){
  if (confirm("Are you sure")){
    console.log(e.targer)
  }
}

form.addEventListener('submit', (e) => {
  console.log(product.value, quantity.value, price.value, created.value)
    e.preventDefault()
    $.ajax({
        type: 'POST',
        url: url,
        data: {
          'csrfmiddlewaretoken': '{{csrf_token}}',
          'product': product.value,
          'quantity': quantity.value,
          'price': price.value,
          'created': created.value
        },

        success: function(response){
            sBtn.style.disabled = false
            updateTabeleRow(response)
            console.log(salesTable.rows.length)
          
        }
    })

})



{/* set sale options */}
const sUrl = '/sales/set-sale/'

const IDs = new Array(1, 2, 3, 4, 5)
console.log(salesTable.rows.length)
if(salesTable.rows.length === 1){
console.log(sBtn)
}
const fin = JSON.stringify(IDs)

sBtn.addEventListener('click', (e) => {

var idList = []

var table = document.getElementById("sale-point-table");
      //iterate trough rows
        for (var i = 0, row; row = table.rows[i]; i++) {
      //iterate trough columns
        for (var j = 0, col; col = row.cells[j]; j++) {
          // do something
          if(col.className === 'position_id') {
            idList.push(col.innerHTML)
          }
      }  
}

console.log(idList)
$.ajax({
  type: 'POST',
  url: sUrl,
  data: {
    'csrfmiddlewaretoken': '{{csrf_token}}',
    'IDs': JSON.stringify(idList),
  },
 
})
})

