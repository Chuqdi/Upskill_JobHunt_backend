import Link from "next/link"
import { useState } from "react";
import { useRouter } from "next/router";

const Candidate = () => {

    const router = useRouter()
    const [candidate, setCandidate] = useState({
        email:'',
        password:'',
        emailError:'',
        passwordError:'',
    })

    const submitHandler = (e) => {
        e.preventDefault()

        candidate.email.length < 1 && 
        candidate.password.length < 1 ?
        setCandidate({...candidate, emailError:'Please input email',  passwordError:'Please input Password'}) : router.push('/plan')

        
    }

    return(
        <section className="py-48 w-full flex">
            <form className="flex flex-col mx-auto justify-center rounded-md shadow-xl w-96 px-4 border-2">
                <h1 className="text-center my-5 font-semibold" style={{color:"#14A800"}}>LOGIN AS A CANDIDATE</h1>
                <div className="py-4 w-full ">
                    <label>Eamil</label><br/>
                    <input className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" type='email' onChange={(e) => setCandidate({...candidate, username:e.target.value})}/>
                    <p className="text-red-600">{candidate.emailError}</p>
                </div>
                <div className="py-4 ">
                    <label>Password</label><br/>
                    <input className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" type='password' onChange={(e) => setCandidate({...candidate, password:e.target.value})}/>
                    <p className="text-red-600">{candidate.passwordError}</p>
                </div>
                <button onClick={submitHandler} className="w-48 mx-auto h-12 text-white rounded-full my-6 text-lg" style={{backgroundColor:"#14A800"}}>Log In</button>
                <div className="flex flex-col">
                        <div className="flex">
                            <h1 className="py-2 pr-1 " style={{color:"#14A800"}}>Dont have an account ?</h1>
                            <Link href="/buisness">
                                <span className="py-2 underline cursor-pointer" style={{color:"#14A800"}}>Sign Up</span>
                            </Link>
                        </div>
                        <Link href="/forget-password/buisness">
                            <h1 className="py-2 pr-2 cursor-pointer" style={{color:"#14A800"}}>ForgetPassword</h1>
                        </Link>
                        
                    </div>
            </form>
        </section>
    )
}
export default Candidate