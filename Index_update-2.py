import React, { useEffect, useState } from 'react';
import { View, FlatList, Text, Image, StyleSheet } from 'react-native';
import { Link } from 'expo-router';

const ListPage = () => {
  const [creators, setCreators] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchCreators = async () => {
    const data = [
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
    ];

    setCreators(data);
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
    flex: 1,
    padding: 20,
    paddingTop: 80,
    backgroundColor: '#000',
    flexGrow: 1,
  },
  card: {
    opacity: 1,
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
});

export default ListPage;
