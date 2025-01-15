import React, { useEffect, useState } from 'react';
import { View, FlatList, Text, Image, StyleSheet, Pressable, Alert, ScrollView } from 'react-native';
import { Link, router } from 'expo-router';
import { AntDesign } from '@expo/vector-icons';
import axios from 'axios';

const ListPage = () => {
  const [creators, setCreators] = useState([]);
  const [loading, setLoading] = useState(true);

  function transformResponse(original: { userId: any; name: any; profileUrl: any; }) {
    return {
      creatorId: original.userId, 
      creatorName: original.name,
      creatorThumbnailURL: original.profileUrl
    };
  }

  const fetchCreators = async () => {
    try {
      const resp = await axios.get('https://zlzq6ogfz7.execute-api.ap-south-1.amazonaws.com/creators');
      const creators = resp.data.creators;
      for (let i = 0; i < creators.length; i++) {
        creators[i] = transformResponse(creators[i]);
      }
      setCreators(creators);
  } catch (error) {
      console.error("Error fetching posts:", error);
      Alert.alert('Something went wrong. Please check your connection and try again.');
  } finally {
      setLoading(false);
  }
    // const data = [
    //   {
    //     creatorId: "1",
    //     creatorName: "Big_Buck_Bunny",
    //     creatorThumbnailURL: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Big_Buck_Bunny_thumbnail_vlc.png/1200px-Big_Buck_Bunny_thumbnail_vlc.png",
    //   },
    //   {
    //     creatorId: "4",
    //     creatorName: "IamKing",
    //     creatorThumbnailURL: "https://i.pinimg.com/736x/1f/97/c2/1f97c2b126afc0cc179294ca7e29f74c.jpg",
    //   },
    //   {
    //     creatorId: "3",
    //     creatorName: "dailyDose",
    //     creatorThumbnailURL: "https://img.jakpost.net/c/2019/09/03/2019_09_03_78912_1567484272._large.jpg",
    //   }
    // ];

    // setCreators(creators);
    setLoading(false);
  };

  useEffect(() => {
    fetchCreators();
  }, []);

  // Render each creator as a card
  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <Link href={`/creator/${item.creatorId}`} style={styles.thumbnailLink}>
        <Image source={{ uri: item.creatorThumbnailURL }} style={styles.thumbnail} />
      </Link>
      <View style={styles.cardContent}>
        <Text style={styles.username}>{item.creatorName}</Text>
        <Text style={styles.bio}>AI Guru</Text>
      </View>
    </View>
  );

  // Show a loading message if data is being fetched
  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <View  style = {styles.listContainer}>

    <View style={styles.arrow}>
        <Pressable 
          style={{ flexDirection: 'row', alignItems: 'center' }}>
          <AntDesign name="user" size={24} color="white" />
        </Pressable>
        <Text style={styles.creatorText}>Creators</Text>
    </View>
      <FlatList
      data={creators}
      renderItem={renderItem}
      keyExtractor={(item) => item.creatorId}
      contentContainerStyle={styles.listContainer}
      pagingEnabled
    />
    {/* //TODO make list scrollable */}
      </View>
  );
};

const styles = StyleSheet.create({
  listContainer: {
    flex: 1,
    padding: 20,
    paddingTop: 50,
    backgroundColor: '#000',
    flexGrow: 1,
  },
  card: {
    opacity: 1,
    backgroundColor: '#000',

    borderRadius: 10,
    borderWidth :1,
    borderColor: '#fff',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    marginBottom: 15,
    flexDirection: 'row',
    padding: 10,
    alignItems: 'center',
  },
  thumbnailLink: {
    marginRight: 10,
  },
  thumbnail: {
    width: 60,
    height: 60,
    borderRadius: 20,
  },
  cardContent: {
    flex: 1,
  },
  username: {
    fontSize: 13,
    fontWeight: 'bold',
    color: 'white',
  },
  bio: {
    fontSize: 10,
    color: '#EEEEEE',
    marginVertical: 3,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  creatorText:{
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
    marginLeft: 16, // Ensures spacing between the icon and text
    flex: 1, // Allows text to occupy remaining space
    textAlign: 'center' // Center the text within the available space
  },
  arrow:{
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 8,
    paddingTop:20,
    position: 'absolute',
    top: 0,
    width: '100%', // Ensures the view spans the top
    zIndex: 10
  },
});

export default ListPage;
