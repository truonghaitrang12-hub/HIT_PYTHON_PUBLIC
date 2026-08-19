const products = [
    {
        id: 1,
        name: "Laptop",
        price: 2000,
        category: "electronics",
        amount: 20
    },
    {
        id: 2,
        name: "Phone",
        price: 1000,
        category: "electronics",
        amount: 2
    },
    {
        id: 3,
        name: "Book",
        price: 20,
        category: "book",
        amount: 10
    },
    {
        id: 4,
        name: "Keyboard",
        price: 100,
        category: "electronics",
        amount: 0
    },
    {
        id: 5,
        name: "Mouse",
        price: 50,
        category: "accessory",
        amount: 15
    }
];
console.log("======= DANH SACH SAN PHAM======= ");
for(const product of products){
    console.log(`ID: ${product.id}|${product.name}| $ ${product.price}|${product.category}|${product.amount}`);
}

console.log(" ======= SAN PHAM CON HANG=======  ");
for(const product of products){
    if (product.amount > 0){
        console.log(product.name);
    }
}

console.log("======= SAN PHAM HET HANG======= ");
for(const product of products){
    if (product.amount == 0){
        console.log(product.name);
    }
}

let totalAmount = 0;
let totalValue = 0;
let totalPrice = 0;

for(const product of products){
    totalAmount += product.amount;
    totalValue += product.price * product.amount;
    totalPrice += product.price;
}
let avergarePrice = totalPrice / products.length;
console.log("CAC SAN PHAM HIEN TAI :");
console.log(`Tong so luong : ${totalAmount}`);
console.log(`Tong gia tri san pham : ${totalValue}`);
console.log(`Gia tri Trung binh :${avergarePrice}`);

let maxProduct = products[0];
for(const product of products){
    if(product.price > maxProduct.price){
        maxProduct = product;
    }
}
console.log(`======= SAN PHAM DAT NHAT=======  \n ${maxProduct.name}, gia : $ ${maxProduct.price}` );

let maxAmount = products[0];
for(const product of products){
    if ( product.amount > maxAmount.amount ){
        maxAmount = product;
    }
}
console.log(`======= SAN PHAM CO SO LUONG LON NHAT=======  \n ${maxAmount.name} ,so luong : ${maxAmount.amount} san pham`);

let findId3 = null;
for(const product of products){
    if(product.id == 3){
        findId3 = product;
    }
}
if (findId3==null){
    console.log("Khong tim thay !")
}else{
    console.log(`======= SAN PHAM CO ID = 3 =======  \n ${findId3.name} `)
}

console.log("======= SAN PHAM THUOC CATEGORY ======= ")
const category = "electronics";
for(const product of products){
    if(product.category === category ){
        console.log(product.name);
    }
}

let countElectronis = 0;
let countBook = 0;
let countAccessory = 0;
for( const product of products){
    if(product.category === "electronics"){
        countElectronis += 1;
    } 
    else if(product.category === "book") {
        countBook += 1;

    }else if (product.category === "accessory"){
        countAccessory += 1;
    }
}
console.log("======= THONG KE SP THUOC CATEGORY ======= ")
console.log(`Electronics: ${countElectronis}`);
console.log(`Book: ${countBook}`);
console.log(`Accessory: ${countAccessory}`);

for(const product of products){
    if (product.price >= 1000){
        console.log(`${product.name} : Cao cap`);

    }else if (product.price >= 100){
        console.log(`${product.name} : Trung binh `);
    }else if(product.price < 100) {
        console.log(`${product.name} : Gia re `);

    }
}