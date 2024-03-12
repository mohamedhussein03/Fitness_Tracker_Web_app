import React from 'react'
import {HiArrowCircleRight} from 'react-icons/hi'

const Home = () => {
  return (
    <div name='home' className='w-full h-screen'>
      <div className='mx-auto w-full max-w-[1000px] px-8 flex flex-col justify-center h-full'>
      <p className='text-xl text-gray-300'>Hey there!</p>
      <h1 className='text-4xl sm:text-7xl font-bold text-[#bd4c72] '>I'm TheRapist</h1>
      <h2 className='text-4xl sm:text-7xl font-bold text-[#d68fa7] '>A TheRapist for issues</h2>
      <p className='py-4 max-w-[700px]'>Basically I give sessions to girls with issues because they are my type, the only difference is
        I love issues.
      </p>
      
      <div>
        <button className=' group border-2 px-6 py-3 my-2 flex items-center  hover:bg-[#d68fa7]'>
          Start Today!
          <span className=' group-hover: duration-300 group-hover:ml-1'>
          <HiArrowCircleRight className='ml-3' />
          </span>
         
        </button>
        </div>
      </div>
    </div>
  )
}

export default Home