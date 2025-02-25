
## **A Secure and Efficient API for Individual Data Retrieval**  

🚀 **This is a powerful and secure API using the Django REST Framework that enables authorized users to retrieve details of individuals using either a National ID or phone number.**  

### 🔒 **Key Security Features**  
✅ **User Authentication** – Every user must log in to obtain an API key for making requests.  
✅ **API Key Validation** – Each request must include a valid API key for access.  
✅ **Request Rate Limiting** – Non-premium users must wait **at least 2 minutes** between requests to optimize resources.  
✅ **Credit-Based System** – Free users start with **10 credits**, which decrease with each successful request. Premium users have **unlimited access**.  
✅ **Access Control** – Unauthorized or excessive requests are blocked to maintain security.  

---

### 🛠️ **How It Works**  

1️⃣ **User Registration & Authentication**  
- Users sign up and log in to obtain an **API key**.  
- The API key is required for all requests.  

2️⃣ **Making a Request**  
- Provide either a **National ID** or **phone number** to retrieve individual details.  
- Non-premium users must **wait 2 minutes** between requests and have **10 credits** (each request deducts 1 credit).  
- **Premium users** have **no limits**.  

3️⃣ **Handling API Responses**  
✔️ **Valid Requests** – Returns the individual’s details.  
❌ **Invalid Requests** – If the user has **insufficient credits** or requests too soon, access is denied.  

---

### 📡 **API Endpoints**  

#### **1️⃣ Check Remaining Credits & Cooldown Time**  
**GET** `/api/check_credits/`  
🔹 Returns available credits and whether the user is on cooldown.  

#### **2️⃣ Retrieve Individual Details**  
**GET** `/api/individual/`  
🔹 Requires **National ID** or **phone number** as a query parameter.  
🔹 Example:  
```sh
curl -X GET "http://127.0.0.1:8000/api/individual/?national_id=123456789" \
     -H "Authorization: Bearer <ACCESS_TOKEN>" \
     -H "X-API-KEY: d4f87b4e6f9e48f99a2c7b935a3d6b51"
```
🔹 **Response:**  
```json
{
  "name": "Godfrey Tankan",
  "national_id": "123456789",
  "age": 30,
  "phone_number": "+263778123456",
  "address": "123 My adress"
}
```

### 🎯 **Why This API?**  
🔹 **High Security** – Strict authentication & rate limiting.  
🔹 **Optimized Performance** – Controls API abuse with credit-based access.  
🔹 **Flexible Access** – Choose between free (limited) or premium (unlimited) usage.  

👨‍💻 **Want to integrate this API or want a similar one into your project? Let’s connect!** 🔗 #Django #API #RESTFramework
