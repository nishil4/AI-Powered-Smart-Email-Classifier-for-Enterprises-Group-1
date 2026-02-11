{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2b629633-20a5-4af4-ad6e-e5af5676edb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>subject</th>\n",
       "      <th>body</th>\n",
       "      <th>text</th>\n",
       "      <th>category</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>promotions_582</td>\n",
       "      <td>Anniversary Special: Buy one get one free</td>\n",
       "      <td>As our loyal customer, get exclusive $60 off $...</td>\n",
       "      <td>Anniversary Special: Buy one get one free As o...</td>\n",
       "      <td>promotions</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>spam_1629</td>\n",
       "      <td>Your Amazon was used on new device</td>\n",
       "      <td>Your $5000 refund is processed. Claim: bit.ly/...</td>\n",
       "      <td>Your Amazon was used on new device Your $5000 ...</td>\n",
       "      <td>spam</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam_322</td>\n",
       "      <td>Re: Your Google inquiry</td>\n",
       "      <td>Hi, following up about your Google application...</td>\n",
       "      <td>Re: Your Google inquiry Hi, following up about...</td>\n",
       "      <td>spam</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>social_media_80</td>\n",
       "      <td>Digital Ritual Experience Creation</td>\n",
       "      <td>Cross-cultural ceremony design. Join: virtualr...</td>\n",
       "      <td>Digital Ritual Experience Creation Cross-cultu...</td>\n",
       "      <td>social_media</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>forum_1351</td>\n",
       "      <td>Your post was moved to \"Programming Help\"</td>\n",
       "      <td>Trending: \"cooking\" (258 comments). View: supp...</td>\n",
       "      <td>Your post was moved to \"Programming Help\" Tren...</td>\n",
       "      <td>forum</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                id                                    subject  \\\n",
       "0   promotions_582  Anniversary Special: Buy one get one free   \n",
       "1        spam_1629         Your Amazon was used on new device   \n",
       "2         spam_322                    Re: Your Google inquiry   \n",
       "3  social_media_80         Digital Ritual Experience Creation   \n",
       "4       forum_1351  Your post was moved to \"Programming Help\"   \n",
       "\n",
       "                                                body  \\\n",
       "0  As our loyal customer, get exclusive $60 off $...   \n",
       "1  Your $5000 refund is processed. Claim: bit.ly/...   \n",
       "2  Hi, following up about your Google application...   \n",
       "3  Cross-cultural ceremony design. Join: virtualr...   \n",
       "4  Trending: \"cooking\" (258 comments). View: supp...   \n",
       "\n",
       "                                                text      category  \\\n",
       "0  Anniversary Special: Buy one get one free As o...    promotions   \n",
       "1  Your Amazon was used on new device Your $5000 ...          spam   \n",
       "2  Re: Your Google inquiry Hi, following up about...          spam   \n",
       "3  Digital Ritual Experience Creation Cross-cultu...  social_media   \n",
       "4  Your post was moved to \"Programming Help\" Tren...         forum   \n",
       "\n",
       "   category_id  \n",
       "0            1  \n",
       "1            3  \n",
       "2            3  \n",
       "3            2  \n",
       "4            0  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"full_dataset.csv\")\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b0aaa29f-5ca7-405a-a42f-7a0fa4be60ac",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 10035 entries, 0 to 13474\n",
      "Data columns (total 8 columns):\n",
      " #   Column            Non-Null Count  Dtype \n",
      "---  ------            --------------  ----- \n",
      " 0   id                10035 non-null  object\n",
      " 1   subject           10035 non-null  object\n",
      " 2   body              10035 non-null  object\n",
      " 3   text              10035 non-null  object\n",
      " 4   category          10035 non-null  object\n",
      " 5   category_id       10035 non-null  int64 \n",
      " 6   clean_text        10035 non-null  object\n",
      " 7   encoded_category  10035 non-null  int64 \n",
      "dtypes: int64(2), object(6)\n",
      "memory usage: 705.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "25f5f9a3-1f3e-4b41-be57-01eb2c6d3e7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                  0\n",
       "subject             0\n",
       "body                0\n",
       "text                0\n",
       "category            0\n",
       "category_id         0\n",
       "clean_text          0\n",
       "encoded_category    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b0d61860-6fc9-49cc-b6d9-a5b3d5c97578",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "category\n",
       "social_media    1998\n",
       "spam            1914\n",
       "updates         1798\n",
       "forum           1742\n",
       "verify_code     1332\n",
       "promotions      1251\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['category'].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ea0530fc-0cac-458a-847b-1e9e420c3e03",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "def clean_text(text):\n",
    "    text = text.lower()                      \n",
    "    text = re.sub(r'http\\S+', '', text)      \n",
    "    text = re.sub(r'[^a-z\\s]', '', text)    \n",
    "    text = re.sub(r'\\s+', ' ', text)         \n",
    "    return text.strip()\n",
    "\n",
    "df['clean_text'] = df['text'].apply(clean_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3d2231fc-7f19-4253-9cdd-1d973b1fcdf2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>text</th>\n",
       "      <th>clean_text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Anniversary Special: Buy one get one free As o...</td>\n",
       "      <td>anniversary special buy one get one free as ou...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Your Amazon was used on new device Your $5000 ...</td>\n",
       "      <td>your amazon was used on new device your refund...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Re: Your Google inquiry Hi, following up about...</td>\n",
       "      <td>re your google inquiry hi following up about y...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Digital Ritual Experience Creation Cross-cultu...</td>\n",
       "      <td>digital ritual experience creation crosscultur...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Your post was moved to \"Programming Help\" Tren...</td>\n",
       "      <td>your post was moved to programming help trendi...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                text  \\\n",
       "0  Anniversary Special: Buy one get one free As o...   \n",
       "1  Your Amazon was used on new device Your $5000 ...   \n",
       "2  Re: Your Google inquiry Hi, following up about...   \n",
       "3  Digital Ritual Experience Creation Cross-cultu...   \n",
       "4  Your post was moved to \"Programming Help\" Tren...   \n",
       "\n",
       "                                          clean_text  \n",
       "0  anniversary special buy one get one free as ou...  \n",
       "1  your amazon was used on new device your refund...  \n",
       "2  re your google inquiry hi following up about y...  \n",
       "3  digital ritual experience creation crosscultur...  \n",
       "4  your post was moved to programming help trendi...  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['text', 'clean_text']].head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e3ed9ab0-6a5e-4a18-9838-7d06372776ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[df['clean_text'].str.len() > 10]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3f1337ad-a036-4038-a83f-cd000b58b0d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop_duplicates(subset=['clean_text'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5fda36bd-ad5f-465e-bc73-3e7a657a3a9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "le = LabelEncoder()\n",
    "df['encoded_category'] = le.fit_transform(df['category'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "85ed219c-88c5-49c8-a8df-f43900705f8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final dataset shape: (10035, 8)\n"
     ]
    }
   ],
   "source": [
    "print(\"Final dataset shape:\", df.shape)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8025535e-4005-4e77-90e9-8a803b71a622",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
