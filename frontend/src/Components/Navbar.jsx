import React , {useState} from 'react'
import {AiOutlineMenu , AiOutlineClose } from 'react-icons/ai'
import { Link } from 'react-scroll'


const Navbar = () => {
  const [nav,setNav] = useState(false)
  const handleChange = () => setNav(!nav)

  return (
    <div  name= " Container " className='flex w-full h-24 max-w-[1240px] mx-auto px-4 items-center justify-between z-100'>
        <h1 className='w-full text-3xl font-bold'> REACT </h1>
      <ul className='hidden md:flex items-center '>
        <li className='p-4  hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link to="home" smooth={true} duration={500}>
          Home
        </Link>
        </li>
        <Link to="about" smooth={true} duration={500}>
        <li className='p-4  hover: cursor-pointer hover:bg-[#d68fa7]'>
          About
        </li>
        </Link>
        <li className='p-4  hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link to="work" smooth={true} duration={500}>
          Work
        </Link>
        </li>
        <li className='p-4  hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link to="contact" smooth={true} duration={500}>
          Contact
        </Link>
        </li>
      </ul>
      <div onClick={handleChange} className='flex md:hidden'>
      {!nav ? <AiOutlineMenu size={20} /> : <AiOutlineClose size={20} />}
      </div>
      <div className={nav ? 'fixed left-0 top-0 w-[60%] h-full border-r border-[#bd4c72] bg-[#250e15]  ease-in-out duration-500' : 'fixed left-[-100%] '}  >
      <h1 className='w-full text-3xl font-bold  m-4 mt-8'> REACT </h1>
      <ul className='upperCase p-4'>
        <li className='p-4 border-b border-[#d68fa7] hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link onClick={handleChange} to="home" smooth={true} duration={500}>
          Home
        </Link>
        </li>
        <li className='p-4 border-b border-[#d68fa7] hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link onClick={handleChange} to="about" smooth={true} duration={500}>
          About
        </Link>
        </li>
        <li className='p-4 border-b border-[#d68fa7] hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link onClick={handleChange} to="work" smooth={true} duration={500}>
          Work
        </Link>
        </li>
        <li className='p-4 border-b border-[#d68fa7] hover: cursor-pointer hover:bg-[#d68fa7]'>
        <Link onClick={handleChange} to="contact" smooth={true} duration={500}>
          Contact
        </Link> 
        </li>
      </ul>
      </div>


    </div>
  )
}

export default Navbar