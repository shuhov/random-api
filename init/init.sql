CREATE TABLE public.resources (
    id serial,
    name text,
    user_agent text
);

ALTER TABLE public.net_params OWNER TO postgres;