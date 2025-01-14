import React, { useEffect, useState } from 'react';
import { View, FlatList, Text, Image, StyleSheet, TouchableOpacity } from 'react-native';
import axios from 'axios';
import { Link } from 'expo-router';

const ListPage = () => {
  const [creators, setCreators] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchCreators = async () => {
    // try {
    //   const response = await axios.get('https://your-api-endpoint/creators'); // Replace with your API endpoint
    //   setCreators(response.data); // Assuming response.data is an array of creators
    //   setLoading(false);
    // } catch (error) {
    //   console.error('Error fetching creators:', error);
    //   setLoading(false);
    // }
    const data: any = [
        {
            creatorId: "1",
            creatorName: "Big_Buck_Bunny",
            creatorThumbnailURL: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Big_Buck_Bunny_thumbnail_vlc.png/1200px-Big_Buck_Bunny_thumbnail_vlc.png",
        },
        {
          creatorId: "4",
          creatorName: "IamKing",
          creatorThumbnailURL: "https://i.pinimg.com/736x/1f/97/c2/1f97c2b126afc0cc179294ca7e29f74c.jpg",
        },
        {
          creatorId: "3",
          creatorName: "dailyDose",
          creatorThumbnailURL: "https://img.jakpost.net/c/2019/09/03/2019_09_03_78912_1567484272._large.jpg",
        }
    ]

    setCreators(data);
    setLoading(false);
  };

  useEffect(() => {
    fetchCreators();
  }, []);

  // Render each creator as a card
  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <Image source={{ uri: item.creatorThumbnailURL }} style={styles.thumbnail} />
      <View style={styles.cardContent}>
        <Text style={styles.username}>{item.creatorName}</Text>
        <Text style={styles.bio}>{"AI Guru"}</Text>
        <Link href={`/creator/${item.creatorId}`} style={styles.link}>
          View Profile
        </Link>
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
    <FlatList
      data={creators}
      renderItem={renderItem}
      keyExtractor={(item) => item.creatorId}
      contentContainerStyle={styles.listContainer}
    />
  );
};

const styles = StyleSheet.create({
  listContainer: {
    flex :1,
    padding: 20,
    paddingTop: 80, //the padding
    backgroundColor: '#000', // the background color
    flexGrow: 1, // ensures that the screen is covered not just the list
  },
  card: {
    opacity: 0.9,
    backgroundColor: '#000',
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    marginBottom: 15,
    flexDirection: 'row',
    padding: 10,
    alignItems: 'center',
  },
  thumbnail: {
    width: 60, // 20 * 2 (size scaling)
    height: 60, // 20 * 2 (size scaling)
    borderRadius: 20,
    marginRight: 10,
    textAlign: 'center',
  },
  cardContent: {
    flex: 1,
    // alignItems: 'center',
  },
  username: {
    fontSize: 13,
    // textAlignVertical: 'center',
    fontWeight: 'bold',
    color: 'white',
    // marginBottom: 5,
    // marginTop: ,
  },
  bio: {
    fontSize: 10,
    color: '#EEEEEE',
    marginVertical: 3,
  },
  link: {
    fontSize: 10,
    color: '#BED754',
    marginTop: 10,
    textAlign: 'center', // Center text
    alignSelf: 'center', // Center within the card content box
    paddingHorizontal: 10, // Add spacing around the button
    paddingVertical: 5, // Add vertical spacing for better appearance
    borderWidth: 1, // Optional: Border for better visibility
    borderColor: '#BED754', // Optional: Border color matching text
    borderRadius: 5,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    
  },
});

export default ListPage;
