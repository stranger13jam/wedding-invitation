CREATE TABLE IF NOT EXISTS public.users (
	id int GENERATED ALWAYS AS IDENTITY NOT NULL,
	first_name text NOT NULL,
	middle_name text NULL,
	last_name text NOT NULL,
	short_name text NULL,
	phone text NULL,
	telegram text NULL,
	"role" text NOT NULL DEFAULT 'guest',
	CONSTRAINT users_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.guests (
	id int GENERATED ALWAYS AS IDENTITY NOT NULL,
	guest_id int NOT NULL,
	partner_id int NULL,
	note text NULL,
	invitation_link text NULL,
	invitation_sent bool DEFAULT false NULL,
	responded_at timestamp NULL,
	will_come bool NULL,
	wishes text NULL,
	CONSTRAINT guests_pk PRIMARY KEY (id),
	CONSTRAINT guests_guest_users_fk FOREIGN KEY (guest_id) REFERENCES public.users("id") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT guests_partner_users_fk FOREIGN KEY (partner_id) REFERENCES public.users("id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS public.contents (
	id int GENERATED ALWAYS AS IDENTITY NOT NULL,
	code text NOT NULL,
	value text NULL,
      language text NOT NULL default 'ru-RU',
	CONSTRAINT contents_pk PRIMARY KEY (id)
);