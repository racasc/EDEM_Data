#### Ejercicios SQL

##### 1\. Provide a SQL that displays the following data: First Name Actor and Last Name Actor Query 
    
    `SELECT first_name, last_name   
    FROM public.actor  
    `

##### 2\. Provide a SQL that displays the following data: Actor Name and Movie Title 
    
    ` SELECT actor.first_name, film.title   
    FROM actor   
    JOIN film_actor ON actor.actor_id = film_actor.actor_id   
    JOIN film ON film_actor.film_id = film.film_id;  
    `

##### 3\. Provide a SQL that displays the following data: Actor Name, Number of movies, Sort from highest to lowest 
    
    ` SELECT actor.first_name, COUNT(actor.first_name)   
    FROM actor JOIN film_actor ON actor.actor_id = film_actor.actor_id JOIN film ON film_actor.film_id = film.film_id   
    GROUP BY actor.first_name  
    ORDER BY 2 DESC;  
    `

##### 4\. Provide a SQL that displays the following data: Movie and Number of times rented 
    
    `SELECT film.title, COUNT(rental.rental_id)   
    FROM film   
    JOIN inventory ON film.film_id = inventory.film_id   
    JOIN rental ON inventory.inventory_id = rental.inventory_id   
    GROUP BY film.title  
    ORDER BY 2 DESC;  
    `

##### 5\. Provide a SQL that displays the following data: Movie and Money grossed per movie 
    
    `SELECT film.title, SUM(payment.amount)   
    FROM film   
    JOIN inventory ON film.film_id = inventory.film_id   
    JOIN rental ON inventory.inventory_id = rental.inventory_id   
    JOIN payment on rental.rental_id = payment.rental_id  
    GROUP BY film.title  
    ORDER BY 2 DESC;  
    `

##### 6\. Provide a SQL that displays the following data: Name of the best customer (highest spend) 
    
    `SELECT customer.first_name,  
    SUM(payment.amount) AS total  
    FROM customer  
    JOIN payment ON customer.customer_id = payment.customer_id  
    GROUP BY customer._id  
    ORDER BY total DESC  
    LIMIT 1;  
    `

##### 7\. Provide a SQL that displays the following data: Name of the best customer (highest number of rentals) 
    
    `SELECT customer.first_name, COUNT(payment.amount) AS total  
    FROM customer  
    JOIN payment ON customer.customer_id = payment.customer_id  
    GROUP BY customer.id  
    ORDER BY total DESC  
    LIMIT 1;  
    `

