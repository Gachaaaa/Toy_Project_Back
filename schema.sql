--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: delivery; Type: TABLE; Schema: public; Owner: sin382382
--

CREATE TABLE public.delivery (
    delivery_id integer NOT NULL,
    user_id integer,
    item_id integer,
    status character varying(50),
    address text,
    scheduled_date date
);


ALTER TABLE public.delivery OWNER TO sin382382;

--
-- Name: delivery_delivery_id_seq; Type: SEQUENCE; Schema: public; Owner: sin382382
--

CREATE SEQUENCE public.delivery_delivery_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.delivery_delivery_id_seq OWNER TO sin382382;

--
-- Name: delivery_delivery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sin382382
--

ALTER SEQUENCE public.delivery_delivery_id_seq OWNED BY public.delivery.delivery_id;


--
-- Name: gacha; Type: TABLE; Schema: public; Owner: sin382382
--

CREATE TABLE public.gacha (
    gacha_id integer NOT NULL,
    title character varying(100) NOT NULL,
    price numeric(10,2) NOT NULL
);


ALTER TABLE public.gacha OWNER TO sin382382;

--
-- Name: gacha_gacha_id_seq; Type: SEQUENCE; Schema: public; Owner: sin382382
--

CREATE SEQUENCE public.gacha_gacha_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.gacha_gacha_id_seq OWNER TO sin382382;

--
-- Name: gacha_gacha_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sin382382
--

ALTER SEQUENCE public.gacha_gacha_id_seq OWNED BY public.gacha.gacha_id;


--
-- Name: gachadraw; Type: TABLE; Schema: public; Owner: sin382382
--

CREATE TABLE public.gachadraw (
    gachadraw_id integer NOT NULL,
    user_id integer,
    gacha_id integer
);


ALTER TABLE public.gachadraw OWNER TO sin382382;

--
-- Name: gachadraw_gachadraw_id_seq; Type: SEQUENCE; Schema: public; Owner: sin382382
--

CREATE SEQUENCE public.gachadraw_gachadraw_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.gachadraw_gachadraw_id_seq OWNER TO sin382382;

--
-- Name: gachadraw_gachadraw_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sin382382
--

ALTER SEQUENCE public.gachadraw_gachadraw_id_seq OWNED BY public.gachadraw.gachadraw_id;


--
-- Name: gachareview; Type: TABLE; Schema: public; Owner: sin382382
--

CREATE TABLE public.gachareview (
    gachareview_id integer NOT NULL,
    gacha_id integer,
    user_id integer,
    review text
);


ALTER TABLE public.gachareview OWNER TO sin382382;

--
-- Name: gachareview_gachareview_id_seq; Type: SEQUENCE; Schema: public; Owner: sin382382
--

CREATE SEQUENCE public.gachareview_gachareview_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.gachareview_gachareview_id_seq OWNER TO sin382382;

--
-- Name: gachareview_gachareview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sin382382
--

ALTER SEQUENCE public.gachareview_gachareview_id_seq OWNED BY public.gachareview.gachareview_id;


--
-- Name: item; Type: TABLE; Schema: public; Owner: sin382382
--

CREATE TABLE public.item (
    item_id integer NOT NULL,
    name character varying(100),
    gacha_id integer,
    quantity integer
);


ALTER TABLE public.item OWNER TO sin382382;

--
-- Name: item_item_id_seq; Type: SEQUENCE; Schema: public; Owner: sin382382
--

CREATE SEQUENCE public.item_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.item_item_id_seq OWNER TO sin382382;

--
-- Name: item_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sin382382
--

ALTER SEQUENCE public.item_item_id_seq OWNED BY public.item.item_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: sin382382
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    login_id character varying(50) NOT NULL,
    password character varying(100) NOT NULL,
    phone_number character varying(20),
    name character varying(50),
    email character varying(100)
);


ALTER TABLE public.users OWNER TO sin382382;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: sin382382
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO sin382382;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sin382382
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: delivery delivery_id; Type: DEFAULT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.delivery ALTER COLUMN delivery_id SET DEFAULT nextval('public.delivery_delivery_id_seq'::regclass);


--
-- Name: gacha gacha_id; Type: DEFAULT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gacha ALTER COLUMN gacha_id SET DEFAULT nextval('public.gacha_gacha_id_seq'::regclass);


--
-- Name: gachadraw gachadraw_id; Type: DEFAULT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachadraw ALTER COLUMN gachadraw_id SET DEFAULT nextval('public.gachadraw_gachadraw_id_seq'::regclass);


--
-- Name: gachareview gachareview_id; Type: DEFAULT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachareview ALTER COLUMN gachareview_id SET DEFAULT nextval('public.gachareview_gachareview_id_seq'::regclass);


--
-- Name: item item_id; Type: DEFAULT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.item ALTER COLUMN item_id SET DEFAULT nextval('public.item_item_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: delivery delivery_pkey; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.delivery
    ADD CONSTRAINT delivery_pkey PRIMARY KEY (delivery_id);


--
-- Name: gacha gacha_pkey; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gacha
    ADD CONSTRAINT gacha_pkey PRIMARY KEY (gacha_id);


--
-- Name: gachadraw gachadraw_pkey; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachadraw
    ADD CONSTRAINT gachadraw_pkey PRIMARY KEY (gachadraw_id);


--
-- Name: gachareview gachareview_pkey; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachareview
    ADD CONSTRAINT gachareview_pkey PRIMARY KEY (gachareview_id);


--
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (item_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_login_id_key; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_login_id_key UNIQUE (login_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: delivery fk_delivery_item; Type: FK CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.delivery
    ADD CONSTRAINT fk_delivery_item FOREIGN KEY (item_id) REFERENCES public.item(item_id) ON DELETE CASCADE;


--
-- Name: delivery fk_delivery_user; Type: FK CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.delivery
    ADD CONSTRAINT fk_delivery_user FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE SET NULL;


--
-- Name: gachadraw fk_draw_gacha; Type: FK CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachadraw
    ADD CONSTRAINT fk_draw_gacha FOREIGN KEY (gacha_id) REFERENCES public.gacha(gacha_id) ON DELETE SET NULL;


--
-- Name: gachareview fk_gacha; Type: FK CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachareview
    ADD CONSTRAINT fk_gacha FOREIGN KEY (gacha_id) REFERENCES public.gacha(gacha_id) ON DELETE CASCADE;


--
-- Name: item fk_item_gacha; Type: FK CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT fk_item_gacha FOREIGN KEY (gacha_id) REFERENCES public.gacha(gacha_id) ON DELETE CASCADE;


--
-- Name: gachareview fk_user; Type: FK CONSTRAINT; Schema: public; Owner: sin382382
--

ALTER TABLE ONLY public.gachareview
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

