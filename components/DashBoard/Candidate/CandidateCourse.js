import Courses from './CandidateComponent/Courses';
import CandidateHoc from './CandidateHoc';
import Pagination from './CandidateComponent/Pagination';
import { useState } from 'react';
import Posts from '../../../post';

const CandidateCourse = () => {

  const [currentPage, setCurrentPage] = useState(1)
  const [postsPerPage, setPostsPerPage] = useState(4)
  const [posts, setPosts] = useState([1,2,3,4,5,6,7,8,9,10])


  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentPosts = Posts.slice(indexOfFirstPost, indexOfLastPost)

  const paginate = (pageNumber) => setCurrentPage(pageNumber)

  console.log(Posts)

    return(

      <CandidateHoc>
        
          <div className="grid xl:grid-cols-2 justify-center">
            {currentPosts.map(post => 
              <Courses key={post.id} title={post.title} time={post.time} description={post.description}/>
            )}
          </div>
          <div className="flex py-8 justify-center  text-white" style={{ marginTop:"50px;"}}>
            <Pagination postsPerPage={postsPerPage} totalPosts={posts.length} paginate={paginate}/>
          </div>
      </CandidateHoc>
            
    )
}

export default CandidateCourse;