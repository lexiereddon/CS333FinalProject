PGDMP  +    !                |           valorantProPlay    14.11 (Homebrew)    16.1     V           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            W           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            X           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            Y           1262    32786    valorantProPlay    DATABASE     s   CREATE DATABASE "valorantProPlay" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
 !   DROP DATABASE "valorantProPlay";
                lexiereddon    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                lexiereddon    false            Z           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   lexiereddon    false    4            �            1259    41000    agentpickrates    TABLE     �   CREATE TABLE public.agentpickrates (
    map character varying NOT NULL,
    agent character varying NOT NULL,
    pick_rate real
);
 "   DROP TABLE public.agentpickrates;
       public         heap    lexiereddon    false    4            �            1259    49178    communityvotes    TABLE     �   CREATE TABLE public.communityvotes (
    user_id bigint NOT NULL,
    most_unlucky character varying,
    most_toxic_team character varying,
    most_tryhard_team character varying
);
 "   DROP TABLE public.communityvotes;
       public         heap    lexiereddon    false    4            �            1259    40993    mapstats    TABLE     �   CREATE TABLE public.mapstats (
    map character varying NOT NULL,
    "totalPicks" integer,
    "groupD" integer,
    "groupC" integer,
    "groupB" integer,
    "groupA" integer,
    playoffs integer,
    atk_wins integer,
    def_wins integer
);
    DROP TABLE public.mapstats;
       public         heap    lexiereddon    false    4            �            1259    32787    matches    TABLE     #  CREATE TABLE public.matches (
    match_id integer,
    game_id integer NOT NULL,
    team character varying NOT NULL,
    score_team integer,
    opponent character varying,
    score_opp integer,
    win_lose character varying,
    map character varying,
    map_pick character varying
);
    DROP TABLE public.matches;
       public         heap    lexiereddon    false    4            �            1259    40986    players    TABLE     �   CREATE TABLE public.players (
    player character varying NOT NULL,
    team character varying,
    nationality character varying,
    role character varying
);
    DROP TABLE public.players;
       public         heap    lexiereddon    false    4            �            1259    32813    playerstats    TABLE     �   CREATE TABLE public.playerstats (
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    player character varying,
    agent character varying,
    acs integer,
    kill integer,
    death integer,
    assist integer
);
    DROP TABLE public.playerstats;
       public         heap    lexiereddon    false    4            �           2606    41006 "   agentpickrates AgentPickRates_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.agentpickrates
    ADD CONSTRAINT "AgentPickRates_pkey" PRIMARY KEY (map, agent);
 N   ALTER TABLE ONLY public.agentpickrates DROP CONSTRAINT "AgentPickRates_pkey";
       public            lexiereddon    false    213    213            �           2606    40999    mapstats MapStats_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.mapstats
    ADD CONSTRAINT "MapStats_pkey" PRIMARY KEY (map);
 B   ALTER TABLE ONLY public.mapstats DROP CONSTRAINT "MapStats_pkey";
       public            lexiereddon    false    212            �           2606    32793    matches Matches_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.matches
    ADD CONSTRAINT "Matches_pkey" PRIMARY KEY (game_id, team);
 @   ALTER TABLE ONLY public.matches DROP CONSTRAINT "Matches_pkey";
       public            lexiereddon    false    209    209            �           2606    32819    playerstats PlayerStats_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.playerstats
    ADD CONSTRAINT "PlayerStats_pkey" PRIMARY KEY (game_id, player_id);
 H   ALTER TABLE ONLY public.playerstats DROP CONSTRAINT "PlayerStats_pkey";
       public            lexiereddon    false    210    210            �           2606    40992    players Players_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.players
    ADD CONSTRAINT "Players_pkey" PRIMARY KEY (player);
 @   ALTER TABLE ONLY public.players DROP CONSTRAINT "Players_pkey";
       public            lexiereddon    false    211            �           2606    49186 "   communityvotes communityvotes_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.communityvotes
    ADD CONSTRAINT communityvotes_pkey PRIMARY KEY (user_id);
 L   ALTER TABLE ONLY public.communityvotes DROP CONSTRAINT communityvotes_pkey;
       public            lexiereddon    false    214           