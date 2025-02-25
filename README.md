## **Secure Individual Data API – Authentication, Rate Limiting & Credit-Based Access**  

This is a **highly secure** API built using Django REST Framework that allows authorized users to **retrieve individual details** using a **National ID or phone number**. With built-in **authentication, API key validation, request limits, and premium access**, this API ensures **efficiency and security**.  

---

### **🔐 Authentication & API Access**  
- Users must **log in** to get an **API key**.  
- Non-premium users get **10 credits**, with each request **deducting 1 credit**.  
- Free users **must wait 2 minutes** between requests.  
- **Premium users have unlimited access.**  

---

## **🌐 API Endpoints & Expected Data**  

### **1️⃣ User Login (Obtain Token & API Key)**
🔹 **Endpoint:**  
```http
POST /api/login/
```
🔹 **Request Body (JSON):**  
```json
{
  "username": "tankan01",
  "password": "securepassword123"
}
```
🔹 **Response (JSON):**  
```json
{
  "token": "abcdef123456...",
  "api_key": "d4f87b4e6f9e48f99a2c7b935a3d6b51",
  "is_premium": false,
  "credits": 10
}
```

---

### **2️⃣ Retrieve Individual Details**  
🔹 **Endpoint:**  
```http
GET /api/individual/
```
🔹 **Request Headers:**  
```http
Authorization: Bearer <ACCESS_TOKEN>
X-API-KEY: d4f87b4e6f9e48f99a2c7b935a3d6b51
```
🔹 **Query Parameters:**  
- `national_id=123456789` **or**  
- `phone_number=+263778123456`  

🔹 **Successful Response (JSON):**  
```json
{
  "name": "Godfrey Tankan",
  "national_id": "123456789",
  "age": 30,
  "phone_number": "+263778123456",
  "address": "123 My own address"
}
```

🔹 **Possible Errors:**  
- `{"detail": "You must wait at least 2 minutes between requests."}` (For non-premium users)  
- `{"detail": "You have run out of credits. Upgrade to premium for unlimited access."}`  
- `{"detail": "No Individual found with the given details."}`
- `{"detail": "Invalid api_token!."}` 

---

### **3️⃣ Check Available Credits & Cooldown**  
🔹 **Endpoint:**  
```http
GET /api/check_credits/
```
🔹 **Request Headers:**  
```http
Authorization: Bearer <ACCESS_TOKEN>
X-API-KEY: d4f87b4e6f9e48f99a2c7b935a3d6b51
```
🔹 **Response:**  
```json
{
  "credits": 5,
  "is_premium": false,
  "can_request_now": false,
  "time_until_next_request": "1 minute 30 seconds"
}
```


## **⚡ Why Use This API?**  
✅ **Secure Authentication** – Every request is protected with API keys & tokens.  
✅ **Optimized Resource Usage** – Limits for free users ensure fair access.  
✅ **Flexible Access** – Free users get limited requests; premium users enjoy unlimited access.  
✅ **Scalable & Reliable** – Built with Django REST Framework for high performance.  

#Django #RESTAPI #Authentication #CyberSecurity #DRF
