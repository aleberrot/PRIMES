const primos = num => {
	divisors = []
	for (let i = 1; i < num; i++){
		if (num % i === 0) divisors.push(i)
	}
	console.log(divisors)
	console.log(divisors.length < 3 ?  `${num} is prime`: `${num} is NOT prime`)
}

primos(99)

const primos_mitad = num =>{
	divisors = []
	for (let i = 1; i < Math.round(num / 2); i++){
		if (num % i === 0) divisors.push(i)
	}
	console.log(divisors)
}

//primos(99)
