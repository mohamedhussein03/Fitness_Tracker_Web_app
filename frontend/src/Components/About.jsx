import React from 'react'

const About = () => {
  return (
    <div name='about' className='w-full h-screen'>
        <div className='flex flex-col justify-center items-center w-full h-full'>
            <div className='max-w-[1000px] w-full grid grid-cols-2 gap-8'>
            <div className='sm:text-right pb-8 pl-4'>
                <h1 className='text-4xl font-bold  inline border-b-4 text-[#bd4c72] border-[#250e15]'> 
            About
            </h1>
            </div>
            <div></div>
            
            </div>
            <div className='max-w-[1000px] w-full grid sm:grid-cols-2 gap-8 px-4'>
            <div className='sm:text-right text-4xl font-bold'>
                <h2> a7a gamed neek
                </h2>
                </div>
                <div>
                    <p className='sm:text-2xl'>here will be the details for the web
                    </p>
                </div>
            </div>
        </div>
    </div>
  )
}

export default About