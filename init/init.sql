CREATE TABLE public.resources (
    id serial,
    name text,
    value text,
    user_agent text
);

ALTER TABLE public.resources OWNER TO postgres;