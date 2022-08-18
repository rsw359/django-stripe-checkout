console.log('Sanity check');

//Get Stripe Perishable Key
fetch("/config")
.then((result) => {return result.json()})
.then((data) => {
  //Initialize Stripe.js
  const stripe= Stripe(data.publicKey); 
});