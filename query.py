# Define the GraphQL query

query = '''
 query($page: Int, $perPage: Int)  {
  Page(page:$page, perPage:$perPage){
    pageInfo{
      total
      currentPage
      lastPage
      hasNextPage
    }
    media(type:MANGA) {
      id
      title{
        english
        native
        romaji
      }
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      status
      genres
      description
      averageScore
      popularity
      
      
    }
  }
}

'''

# Define our query variables and values that will be used in the query request
variables = {
    'page': 1,
    'perPage': 100
}

# API url 
url = 'https://graphql.anilist.co'