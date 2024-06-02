import express from "express";
import cors from "cors";
import mongoose from "mongoose";

const PORT = process.env.PORT || 5050;
const app = express();


app.use(cors());
app.use(express.json());

mongoose.connect('mongodb+srv://ngoth:cs361databasepass@passcluster.aq8huj0.mongodb.net/', () => {
    console.log("DB connected.");
});


function generatePassword() {
    let password = '';
    let symbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
        'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '!%&@#$';
 
    for (let i = 1; i <= 10; i++) {
        let char = Math.floor(Math.random()
            * symbol.length + 1);
 
        password += symbol.charAt(char)
    }
 
    return password;
}

// create password 
app.post('/', (req, res) => {
  res.send(generatePassword())
})


app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});



